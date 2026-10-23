# EMA Hourly Continuation — ARKM/USDT P12_144

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8817 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -2.8174 |
| sortino_ratio | -0.8333 |
| max_drawdown | 0.6395 |
| cagr | -0.3275 |
| net_avg_win | 56.7436 |
| net_avg_loss | -75.2994 |
| avg_hold_time_bars | 35.1528 |
| exposure | 0.7110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
