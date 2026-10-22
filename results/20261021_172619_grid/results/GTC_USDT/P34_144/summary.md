# EMA Hourly Continuation — GTC/USDT P34_144

**Symbol:** GTC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.6790 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8393 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -2.5003 |
| sortino_ratio | -0.6958 |
| max_drawdown | 0.5923 |
| cagr | -0.2745 |
| net_avg_win | 66.8736 |
| net_avg_loss | -81.6885 |
| avg_hold_time_bars | 22.7254 |
| exposure | 0.3987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
