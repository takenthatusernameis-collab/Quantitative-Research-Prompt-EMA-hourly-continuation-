# EMA Hourly Continuation — BCH/USDT P55_144

**Symbol:** BCH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -4.1820 |
| sortino_ratio | -1.3356 |
| max_drawdown | 0.8112 |
| cagr | -0.4715 |
| net_avg_win | 44.4845 |
| net_avg_loss | -69.1133 |
| avg_hold_time_bars | 10.7667 |
| exposure | 0.2496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
