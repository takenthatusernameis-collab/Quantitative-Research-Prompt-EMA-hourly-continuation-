# EMA Hourly Continuation — NYM/USDT P12_144

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.3414 |
| net_win_rate | 0.3452 |
| gross_profit_factor | 0.5846 |
| gross_win_rate | 0.3591 |
| sharpe_ratio | -7.6007 |
| sortino_ratio | -2.4066 |
| max_drawdown | 0.9527 |
| cagr | -0.7002 |
| net_avg_win | 28.3439 |
| net_avg_loss | -43.7764 |
| avg_hold_time_bars | 28.9067 |
| exposure | 0.6622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
