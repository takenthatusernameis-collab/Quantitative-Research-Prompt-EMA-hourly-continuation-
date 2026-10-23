# EMA Hourly Continuation — ZETA/USDT P12_26

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1386 |
| net_profit_factor | 0.4126 |
| net_win_rate | 0.4177 |
| gross_profit_factor | 0.8122 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -10.6827 |
| sortino_ratio | -5.6120 |
| max_drawdown | 0.9991 |
| cagr | -0.9376 |
| net_avg_win | 12.1229 |
| net_avg_loss | -21.0781 |
| avg_hold_time_bars | 3.1270 |
| exposure | 0.1961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
