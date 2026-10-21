# EMA Hourly Continuation — VR/USDT P20_26

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 171 |
| net_profit_factor | 0.5696 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.8678 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -2.6060 |
| sortino_ratio | -0.4829 |
| max_drawdown | 0.4523 |
| cagr | -0.2031 |
| net_avg_win | 79.8556 |
| net_avg_loss | -101.9673 |
| avg_hold_time_bars | 6.6316 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
