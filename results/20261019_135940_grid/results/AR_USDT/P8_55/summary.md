# EMA Hourly Continuation — AR/USDT P8_55

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.5703 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8446 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -4.9282 |
| sortino_ratio | -2.1035 |
| max_drawdown | 0.9254 |
| cagr | -0.6377 |
| net_avg_win | 28.5866 |
| net_avg_loss | -43.3410 |
| avg_hold_time_bars | 12.9003 |
| exposure | 0.5412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
