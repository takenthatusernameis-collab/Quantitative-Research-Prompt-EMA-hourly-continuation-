# EMA Hourly Continuation — ARB/USDT P8_200

**Symbol:** ARB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 1.2211 |
| net_win_rate | 0.5808 |
| gross_profit_factor | 1.3727 |
| gross_win_rate | 0.5808 |
| sharpe_ratio | 0.7935 |
| sortino_ratio | 0.1504 |
| max_drawdown | 0.0633 |
| cagr | 0.0628 |
| net_avg_win | 94.1811 |
| net_avg_loss | -106.8781 |
| avg_hold_time_bars | 115.1018 |
| exposure | 0.8737 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
