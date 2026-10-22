# EMA Hourly Continuation — ZK/USDT P12_21

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1407 |
| net_profit_factor | 0.4839 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.9791 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -11.5522 |
| sortino_ratio | -6.3346 |
| max_drawdown | 0.9994 |
| cagr | -0.9580 |
| net_avg_win | 16.0472 |
| net_avg_loss | -23.5305 |
| avg_hold_time_bars | 2.4293 |
| exposure | 0.1666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
