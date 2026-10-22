# EMA Hourly Continuation — ETH/USDT P34_100

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.4169 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.9018 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -6.4453 |
| sortino_ratio | -2.2291 |
| max_drawdown | 0.9432 |
| cagr | -0.6778 |
| net_avg_win | 24.4014 |
| net_avg_loss | -48.8007 |
| avg_hold_time_bars | 10.6227 |
| exposure | 0.2931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
