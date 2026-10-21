# EMA Hourly Continuation — INJ/USDT P100_144

**Symbol:** INJ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9695 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -1.3177 |
| sortino_ratio | -0.2819 |
| max_drawdown | 0.3303 |
| cagr | -0.1217 |
| net_avg_win | 77.0055 |
| net_avg_loss | -99.5683 |
| avg_hold_time_bars | 6.2152 |
| exposure | 0.0630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
