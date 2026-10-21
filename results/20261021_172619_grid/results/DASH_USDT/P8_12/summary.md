# EMA Hourly Continuation — DASH/USDT P8_12

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.6038 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -1.9900 |
| sortino_ratio | -0.3991 |
| max_drawdown | 0.3876 |
| cagr | -0.1680 |
| net_avg_win | 60.6034 |
| net_avg_loss | -90.6295 |
| avg_hold_time_bars | 3.8214 |
| exposure | 0.0340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
