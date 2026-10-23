# EMA Hourly Continuation — YGG/USDT P12_144

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6440 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9023 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -3.2772 |
| sortino_ratio | -1.0736 |
| max_drawdown | 0.7361 |
| cagr | -0.4019 |
| net_avg_win | 51.3422 |
| net_avg_loss | -69.8944 |
| avg_hold_time_bars | 26.1423 |
| exposure | 0.6483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
