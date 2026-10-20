# EMA Hourly Continuation — CFG/USDT P26_55

**Symbol:** CFG/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.4672 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8498 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -5.9864 |
| sortino_ratio | -2.2432 |
| max_drawdown | 0.9381 |
| cagr | -0.6655 |
| net_avg_win | 26.3084 |
| net_avg_loss | -43.8132 |
| avg_hold_time_bars | 11.9285 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
