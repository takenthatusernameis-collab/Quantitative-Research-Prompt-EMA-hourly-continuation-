# EMA Hourly Continuation — ICP/USDT P21_100

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.8118 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0136 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.5256 |
| sortino_ratio | -0.4891 |
| max_drawdown | 0.4834 |
| cagr | -0.2027 |
| net_avg_win | 74.2710 |
| net_avg_loss | -92.5874 |
| avg_hold_time_bars | 16.8962 |
| exposure | 0.3848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
