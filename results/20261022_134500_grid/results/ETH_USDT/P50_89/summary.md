# EMA Hourly Continuation — ETH/USDT P50_89

**Symbol:** ETH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.3487 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.9652 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -8.0741 |
| sortino_ratio | -2.9253 |
| max_drawdown | 0.9779 |
| cagr | -0.7792 |
| net_avg_win | 18.5598 |
| net_avg_loss | -41.0073 |
| avg_hold_time_bars | 4.4043 |
| exposure | 0.1297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
