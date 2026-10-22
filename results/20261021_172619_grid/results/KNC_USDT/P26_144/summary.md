# EMA Hourly Continuation — KNC/USDT P26_144

**Symbol:** KNC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.8207 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0590 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.2933 |
| sortino_ratio | -0.3648 |
| max_drawdown | 0.4571 |
| cagr | -0.1554 |
| net_avg_win | 79.9308 |
| net_avg_loss | -102.5699 |
| avg_hold_time_bars | 27.4223 |
| exposure | 0.4811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
