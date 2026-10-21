# EMA Hourly Continuation — ETH/USDT P8_26

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6718 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0401 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -2.8642 |
| sortino_ratio | -0.9545 |
| max_drawdown | 0.6748 |
| cagr | -0.3522 |
| net_avg_win | 49.7802 |
| net_avg_loss | -77.2090 |
| avg_hold_time_bars | 7.1458 |
| exposure | 0.1738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
