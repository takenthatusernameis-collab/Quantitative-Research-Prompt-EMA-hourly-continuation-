# EMA Hourly Continuation — AMP/USDT P50_200

**Symbol:** AMP/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.4208 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.6687 |
| gross_win_rate | 0.4238 |
| sharpe_ratio | -5.5779 |
| sortino_ratio | -1.8582 |
| max_drawdown | 0.9001 |
| cagr | -0.5930 |
| net_avg_win | 27.6823 |
| net_avg_loss | -46.9885 |
| avg_hold_time_bars | 16.3387 |
| exposure | 0.4189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
