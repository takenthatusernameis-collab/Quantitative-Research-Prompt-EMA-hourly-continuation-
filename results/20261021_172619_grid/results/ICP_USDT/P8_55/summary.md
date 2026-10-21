# EMA Hourly Continuation — ICP/USDT P8_55

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.8408 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0697 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -1.4852 |
| sortino_ratio | -0.5618 |
| max_drawdown | 0.5147 |
| cagr | -0.2301 |
| net_avg_win | 71.2397 |
| net_avg_loss | -90.2902 |
| avg_hold_time_bars | 13.1691 |
| exposure | 0.4142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
