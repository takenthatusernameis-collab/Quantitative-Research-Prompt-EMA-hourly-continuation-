# EMA Hourly Continuation — ENS/USDT P34_89

**Symbol:** ENS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7912 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0505 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.6088 |
| sortino_ratio | -0.4826 |
| max_drawdown | 0.5000 |
| cagr | -0.1993 |
| net_avg_win | 72.6786 |
| net_avg_loss | -96.1702 |
| avg_hold_time_bars | 11.5849 |
| exposure | 0.2296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
