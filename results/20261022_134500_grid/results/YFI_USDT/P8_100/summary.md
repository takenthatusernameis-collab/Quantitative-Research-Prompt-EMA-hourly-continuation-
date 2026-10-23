# EMA Hourly Continuation — YFI/USDT P8_100

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.5334 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -4.9210 |
| sortino_ratio | -1.7830 |
| max_drawdown | 0.8935 |
| cagr | -0.5856 |
| net_avg_win | 32.1574 |
| net_avg_loss | -52.7899 |
| avg_hold_time_bars | 22.2474 |
| exposure | 0.6836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
