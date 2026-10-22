# EMA Hourly Continuation — MEW/USDT P34_89

**Symbol:** MEW/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6799 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8488 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -2.4440 |
| sortino_ratio | -0.7321 |
| max_drawdown | 0.5690 |
| cagr | -0.2848 |
| net_avg_win | 58.6587 |
| net_avg_loss | -74.9959 |
| avg_hold_time_bars | 10.0880 |
| exposure | 0.2031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
