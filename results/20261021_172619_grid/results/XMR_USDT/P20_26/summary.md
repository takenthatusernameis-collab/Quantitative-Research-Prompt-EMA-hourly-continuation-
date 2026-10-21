# EMA Hourly Continuation — XMR/USDT P20_26

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.4644 |
| net_win_rate | 0.3980 |
| gross_profit_factor | 0.6570 |
| gross_win_rate | 0.3980 |
| sharpe_ratio | -2.2978 |
| sortino_ratio | -0.3242 |
| max_drawdown | 0.3276 |
| cagr | -0.1394 |
| net_avg_win | 69.8236 |
| net_avg_loss | -99.3872 |
| avg_hold_time_bars | 4.8571 |
| exposure | 0.0216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
