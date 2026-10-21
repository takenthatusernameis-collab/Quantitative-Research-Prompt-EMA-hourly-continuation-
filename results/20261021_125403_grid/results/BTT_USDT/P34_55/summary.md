# EMA Hourly Continuation — BTT/USDT P34_55

**Symbol:** BTT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.3725 |
| net_win_rate | 0.3975 |
| gross_profit_factor | 0.6866 |
| gross_win_rate | 0.3975 |
| sharpe_ratio | -5.6695 |
| sortino_ratio | -1.4723 |
| max_drawdown | 0.8285 |
| cagr | -0.5011 |
| net_avg_win | 38.9020 |
| net_avg_loss | -68.8873 |
| avg_hold_time_bars | 7.2366 |
| exposure | 0.1043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
