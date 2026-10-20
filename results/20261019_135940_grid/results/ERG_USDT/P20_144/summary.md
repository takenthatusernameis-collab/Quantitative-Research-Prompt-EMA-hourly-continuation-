# EMA Hourly Continuation — ERG/USDT P20_144

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.4725 |
| net_win_rate | 0.4250 |
| gross_profit_factor | 0.7074 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -5.2195 |
| sortino_ratio | -1.7877 |
| max_drawdown | 0.8871 |
| cagr | -0.5765 |
| net_avg_win | 31.4335 |
| net_avg_loss | -49.1652 |
| avg_hold_time_bars | 18.2867 |
| exposure | 0.4929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
