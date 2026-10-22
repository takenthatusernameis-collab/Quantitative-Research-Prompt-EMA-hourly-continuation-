# EMA Hourly Continuation — DODO/USDT P12_20

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6256 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -3.1762 |
| sortino_ratio | -0.9703 |
| max_drawdown | 0.6752 |
| cagr | -0.3586 |
| net_avg_win | 51.8793 |
| net_avg_loss | -74.9807 |
| avg_hold_time_bars | 5.0241 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
