# EMA Hourly Continuation — ICP/USDT P50_144

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.7557 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9543 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.5931 |
| sortino_ratio | -0.4140 |
| max_drawdown | 0.3953 |
| cagr | -0.1735 |
| net_avg_win | 72.6039 |
| net_avg_loss | -92.0989 |
| avg_hold_time_bars | 18.4804 |
| exposure | 0.2780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
