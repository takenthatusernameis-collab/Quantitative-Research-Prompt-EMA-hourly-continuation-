# EMA Hourly Continuation — BCH/USDT P34_144

**Symbol:** BCH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.5860 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9876 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -3.9890 |
| sortino_ratio | -1.2248 |
| max_drawdown | 0.8050 |
| cagr | -0.4523 |
| net_avg_win | 47.9637 |
| net_avg_loss | -74.4128 |
| avg_hold_time_bars | 19.1739 |
| exposure | 0.4210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
