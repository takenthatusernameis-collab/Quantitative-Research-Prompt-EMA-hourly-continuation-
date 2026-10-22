# EMA Hourly Continuation — ENS/USDT P12_144

**Symbol:** ENS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6795 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9528 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -2.2084 |
| sortino_ratio | -0.6536 |
| max_drawdown | 0.5643 |
| cagr | -0.2663 |
| net_avg_win | 52.3339 |
| net_avg_loss | -76.6638 |
| avg_hold_time_bars | 36.3759 |
| exposure | 0.7259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
