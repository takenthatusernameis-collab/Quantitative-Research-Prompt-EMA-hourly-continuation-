# EMA Hourly Continuation — ETH/USDT P12_21

**Symbol:** ETH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.7007 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.1224 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -1.7555 |
| sortino_ratio | -0.4017 |
| max_drawdown | 0.4009 |
| cagr | -0.1666 |
| net_avg_win | 65.1579 |
| net_avg_loss | -104.0168 |
| avg_hold_time_bars | 5.3480 |
| exposure | 0.0608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
