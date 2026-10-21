# EMA Hourly Continuation — IMX/USDT P20_89

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.8812 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0702 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -0.7805 |
| sortino_ratio | -0.2468 |
| max_drawdown | 0.2764 |
| cagr | -0.1113 |
| net_avg_win | 75.7534 |
| net_avg_loss | -92.9794 |
| avg_hold_time_bars | 17.5155 |
| exposure | 0.3844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
