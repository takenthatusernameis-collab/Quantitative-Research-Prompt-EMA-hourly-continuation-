# EMA Hourly Continuation — CAKE/USDT P26_89

**Symbol:** CAKE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.8273 |
| net_win_rate | 0.5252 |
| gross_profit_factor | 1.1142 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -1.2941 |
| sortino_ratio | -0.3981 |
| max_drawdown | 0.4160 |
| cagr | -0.1689 |
| net_avg_win | 74.1510 |
| net_avg_loss | -99.1326 |
| avg_hold_time_bars | 15.3720 |
| exposure | 0.3193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
