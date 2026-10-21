# EMA Hourly Continuation — CRV/USDT P34_89

**Symbol:** CRV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.8090 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0188 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.4234 |
| sortino_ratio | -0.4228 |
| max_drawdown | 0.4289 |
| cagr | -0.1775 |
| net_avg_win | 76.0511 |
| net_avg_loss | -95.3271 |
| avg_hold_time_bars | 10.2681 |
| exposure | 0.2002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
