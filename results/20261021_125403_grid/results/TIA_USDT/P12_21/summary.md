# EMA Hourly Continuation — TIA/USDT P12_21

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7449 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9732 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.4751 |
| sortino_ratio | -0.3572 |
| max_drawdown | 0.3981 |
| cagr | -0.1514 |
| net_avg_win | 69.4968 |
| net_avg_loss | -92.6439 |
| avg_hold_time_bars | 4.5053 |
| exposure | 0.0584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
