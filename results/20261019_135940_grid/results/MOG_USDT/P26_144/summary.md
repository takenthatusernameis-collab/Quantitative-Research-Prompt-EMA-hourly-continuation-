# EMA Hourly Continuation — MOG/USDT P26_144

**Symbol:** MOG/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -3.1605 |
| sortino_ratio | -1.0099 |
| max_drawdown | 0.7120 |
| cagr | -0.3847 |
| net_avg_win | 61.6164 |
| net_avg_loss | -79.9308 |
| avg_hold_time_bars | 18.8643 |
| exposure | 0.4492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
