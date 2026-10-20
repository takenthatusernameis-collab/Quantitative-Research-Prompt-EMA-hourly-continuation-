# EMA Hourly Continuation — ATH/USDT P8_50

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1094 |
| net_profit_factor | 0.6531 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0047 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -4.5412 |
| sortino_ratio | -2.1708 |
| max_drawdown | 0.9205 |
| cagr | -0.6512 |
| net_avg_win | 31.4185 |
| net_avg_loss | -48.4621 |
| avg_hold_time_bars | 8.2075 |
| exposure | 0.4352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
