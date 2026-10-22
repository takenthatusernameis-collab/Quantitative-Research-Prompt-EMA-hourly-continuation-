# EMA Hourly Continuation — NOT/USDT P12_20

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 1.0163 |
| net_win_rate | 0.5748 |
| gross_profit_factor | 1.3372 |
| gross_win_rate | 0.5748 |
| sharpe_ratio | 0.1216 |
| sortino_ratio | 0.0265 |
| max_drawdown | 0.1125 |
| cagr | 0.0070 |
| net_avg_win | 87.1748 |
| net_avg_loss | -115.9449 |
| avg_hold_time_bars | 5.4019 |
| exposure | 0.0543 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
