# EMA Hourly Continuation — ETH/USDT P8_55

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6791 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.7958 |
| sortino_ratio | -0.9448 |
| max_drawdown | 0.6692 |
| cagr | -0.3506 |
| net_avg_win | 51.3033 |
| net_avg_loss | -72.6209 |
| avg_hold_time_bars | 17.8959 |
| exposure | 0.4531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
