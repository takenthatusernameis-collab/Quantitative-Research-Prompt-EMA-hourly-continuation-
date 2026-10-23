# EMA Hourly Continuation — MANTA/USDT P12_200

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7264 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9720 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -1.9727 |
| sortino_ratio | -0.4949 |
| max_drawdown | 0.4981 |
| cagr | -0.2089 |
| net_avg_win | 77.1679 |
| net_avg_loss | -97.9163 |
| avg_hold_time_bars | 53.5235 |
| exposure | 0.7761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
