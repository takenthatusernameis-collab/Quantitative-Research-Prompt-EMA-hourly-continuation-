# EMA Hourly Continuation — BCH/USDT P12_200

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7096 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.1157 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -2.2912 |
| sortino_ratio | -0.5903 |
| max_drawdown | 0.5782 |
| cagr | -0.2470 |
| net_avg_win | 73.6797 |
| net_avg_loss | -104.4467 |
| avg_hold_time_bars | 48.5401 |
| exposure | 0.7435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
