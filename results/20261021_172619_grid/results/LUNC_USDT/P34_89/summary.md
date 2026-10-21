# EMA Hourly Continuation — LUNC/USDT P34_89

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6615 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.8838 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -2.4485 |
| sortino_ratio | -0.7238 |
| max_drawdown | 0.5905 |
| cagr | -0.2818 |
| net_avg_win | 53.8153 |
| net_avg_loss | -74.7827 |
| avg_hold_time_bars | 10.7266 |
| exposure | 0.2087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
