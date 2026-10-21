# EMA Hourly Continuation — GRT/USDT P144_200

**Symbol:** GRT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 174 |
| net_profit_factor | 0.6137 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8252 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -1.8870 |
| sortino_ratio | -0.3545 |
| max_drawdown | 0.3527 |
| cagr | -0.1500 |
| net_avg_win | 66.7612 |
| net_avg_loss | -92.5887 |
| avg_hold_time_bars | 7.4828 |
| exposure | 0.0589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
