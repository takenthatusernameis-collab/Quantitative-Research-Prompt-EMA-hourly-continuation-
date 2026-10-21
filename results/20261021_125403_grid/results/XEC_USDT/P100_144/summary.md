# EMA Hourly Continuation — XEC/USDT P100_144

**Symbol:** XEC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.5753 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8736 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.8967 |
| sortino_ratio | -0.6906 |
| max_drawdown | 0.5586 |
| cagr | -0.2721 |
| net_avg_win | 57.8810 |
| net_avg_loss | -87.0993 |
| avg_hold_time_bars | 6.8094 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
