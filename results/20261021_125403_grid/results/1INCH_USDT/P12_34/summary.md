# EMA Hourly Continuation — 1INCH/USDT P12_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.6147 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.8686 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -3.7092 |
| sortino_ratio | -1.3340 |
| max_drawdown | 0.7877 |
| cagr | -0.4570 |
| net_avg_win | 41.8380 |
| net_avg_loss | -61.1166 |
| avg_hold_time_bars | 7.2579 |
| exposure | 0.2085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
