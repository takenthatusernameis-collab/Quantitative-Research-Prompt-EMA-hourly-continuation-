# EMA Hourly Continuation — ZRX/USDT P12_200

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.8003 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3149 |
| sortino_ratio | -0.3428 |
| max_drawdown | 0.3645 |
| cagr | -0.1477 |
| net_avg_win | 79.3304 |
| net_avg_loss | -99.1200 |
| avg_hold_time_bars | 46.4850 |
| exposure | 0.7057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
