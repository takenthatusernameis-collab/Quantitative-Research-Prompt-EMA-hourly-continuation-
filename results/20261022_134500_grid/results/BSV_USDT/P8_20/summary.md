# EMA Hourly Continuation — BSV/USDT P8_20

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1797 |
| net_profit_factor | 0.2960 |
| net_win_rate | 0.3901 |
| gross_profit_factor | 0.8034 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -15.4295 |
| sortino_ratio | -9.3539 |
| max_drawdown | 1.0000 |
| cagr | -0.9919 |
| net_avg_win | 5.9980 |
| net_avg_loss | -12.9603 |
| avg_hold_time_bars | 2.8303 |
| exposure | 0.2312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
