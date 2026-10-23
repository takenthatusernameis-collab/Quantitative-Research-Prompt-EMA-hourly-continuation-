# EMA Hourly Continuation — TRADE/USDT P26_89

**Symbol:** TRADE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.5521 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8480 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -4.4227 |
| sortino_ratio | -1.4697 |
| max_drawdown | 0.8444 |
| cagr | -0.5198 |
| net_avg_win | 40.2002 |
| net_avg_loss | -60.0209 |
| avg_hold_time_bars | 11.4588 |
| exposure | 0.2974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
