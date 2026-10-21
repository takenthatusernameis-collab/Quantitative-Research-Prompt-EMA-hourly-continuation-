# EMA Hourly Continuation — ICP/USDT P26_34

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.7636 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0922 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -1.0430 |
| sortino_ratio | -0.1875 |
| max_drawdown | 0.2386 |
| cagr | -0.0823 |
| net_avg_win | 77.3456 |
| net_avg_loss | -110.8789 |
| avg_hold_time_bars | 4.9226 |
| exposure | 0.0347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
