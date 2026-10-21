# EMA Hourly Continuation — SUN/USDT P12_34

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.4703 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8627 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -6.9892 |
| sortino_ratio | -2.6001 |
| max_drawdown | 0.9570 |
| cagr | -0.7128 |
| net_avg_win | 28.3184 |
| net_avg_loss | -48.6951 |
| avg_hold_time_bars | 8.0477 |
| exposure | 0.2444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
