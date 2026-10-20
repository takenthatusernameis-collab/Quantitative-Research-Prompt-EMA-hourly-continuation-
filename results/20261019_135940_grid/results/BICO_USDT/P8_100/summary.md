# EMA Hourly Continuation — BICO/USDT P8_100

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.7680 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 1.0171 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -2.1244 |
| sortino_ratio | -0.7402 |
| max_drawdown | 0.6282 |
| cagr | -0.2927 |
| net_avg_win | 65.1750 |
| net_avg_loss | -81.8140 |
| avg_hold_time_bars | 25.3943 |
| exposure | 0.6937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
