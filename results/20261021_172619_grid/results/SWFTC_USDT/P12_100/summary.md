# EMA Hourly Continuation — SWFTC/USDT P12_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.7378 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8991 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -2.2659 |
| sortino_ratio | -0.7350 |
| max_drawdown | 0.5888 |
| cagr | -0.2865 |
| net_avg_win | 65.6589 |
| net_avg_loss | -79.2820 |
| avg_hold_time_bars | 18.8885 |
| exposure | 0.4465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
