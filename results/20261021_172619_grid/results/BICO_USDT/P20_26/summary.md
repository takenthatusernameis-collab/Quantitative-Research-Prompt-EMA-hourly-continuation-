# EMA Hourly Continuation — BICO/USDT P20_26

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6192 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.9040 |
| sortino_ratio | -0.7900 |
| max_drawdown | 0.6066 |
| cagr | -0.3032 |
| net_avg_win | 56.7239 |
| net_avg_loss | -82.4421 |
| avg_hold_time_bars | 4.8006 |
| exposure | 0.0788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
