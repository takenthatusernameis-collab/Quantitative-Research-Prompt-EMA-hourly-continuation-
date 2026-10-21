# EMA Hourly Continuation — APT/USDT P55_144

**Symbol:** APT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8735 |
| net_win_rate | 0.5287 |
| gross_profit_factor | 1.1042 |
| gross_win_rate | 0.5287 |
| sharpe_ratio | -0.6844 |
| sortino_ratio | -0.1843 |
| max_drawdown | 0.2482 |
| cagr | -0.0837 |
| net_avg_win | 73.9709 |
| net_avg_loss | -95.0135 |
| avg_hold_time_bars | 13.6724 |
| exposure | 0.2163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
