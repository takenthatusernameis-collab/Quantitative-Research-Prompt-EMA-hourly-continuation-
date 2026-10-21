# EMA Hourly Continuation — MANA/USDT P8_55

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.7675 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -2.3011 |
| sortino_ratio | -0.8324 |
| max_drawdown | 0.6326 |
| cagr | -0.3179 |
| net_avg_win | 64.7073 |
| net_avg_loss | -81.9655 |
| avg_hold_time_bars | 16.3020 |
| exposure | 0.4735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
